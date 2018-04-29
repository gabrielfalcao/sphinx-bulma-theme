var path = require("path");

module.exports = {
    entry: './sphinx_bulma_theme/sphinx-bulma.src.js',
    output: {
        filename: 'theme.js',
        path: path.resolve(__dirname, 'sphinx_bulma_theme/static/js/')
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                use: {
                    loader: "babel-loader",
                    options: {
                        presets: [
                            "env",
                            "stage-0",
                            "react-app"
                        ]
                    }
                }
            },
            {
                test: /[.](s?css|sass)$/i,
                use: [
                    {
                        loader: "style-loader" // creates style nodes from JS strings
                    },
                    {
                        loader: "css-loader" // translates CSS into CommonJS
                    },
                    {
                        loader: "sass-loader" // compiles Sass to CSS
                    }
                ]
            }
        ]
    }
};
