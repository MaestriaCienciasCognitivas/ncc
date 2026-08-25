import path from 'node:path';

const REPO = 'MaestriaCienciasCognitivas/ncc';
const BRANCH = 'main';

const colabTransform = {
  name: 'add-colab-button',
  doc: 'Automatically add an Open in Colab badge to notebook pages.',
  stage: 'document',

  plugin: () => (tree, vfile) => {
    // Ruta del documento que MyST está procesando
    const filename = vfile?.path;

    // Solo actuar sobre notebooks
    if (!filename || !filename.endsWith('.ipynb')) {
      return;
    }

    /*
     * El build se ejecuta desde book/, por lo que nos interesa obtener
     * una ruta como:
     *
     * notebooks/S1_Cuaderno1.ipynb
     */
    let relativePath = path.relative(process.cwd(), filename);

    // Normalizar separadores por si se ejecuta en otro sistema operativo
    relativePath = relativePath.split(path.sep).join('/');

    // Si por alguna razón aparece "book/" al principio, eliminarlo,
    // porque lo añadimos explícitamente en la URL de GitHub.
    relativePath = relativePath.replace(/^book\//, '');

    const colabUrl =
      `https://colab.research.google.com/github/${REPO}` +
      `/blob/${BRANCH}/book/${relativePath}`;

    const badge = {
      type: 'paragraph',
      children: [
        {
          type: 'link',
          url: colabUrl,
          children: [
            {
              type: 'image',
              url: 'https://colab.research.google.com/assets/colab-badge.svg',
              alt: 'Abrir en Colab',
              align: 'left',
            },
          ],
        },
      ],
    };

    // Poner el badge después del título, si existe.
    const firstHeading = tree.children.findIndex(
      (node) => node.type === 'heading'
    );

    if (firstHeading >= 0) {
      tree.children.splice(firstHeading + 1, 0, badge);
    } else {
      tree.children.unshift(badge);
    }
  },
};

const plugin = {
  name: 'Google Colab buttons',
  transforms: [colabTransform],
};

export default plugin;
