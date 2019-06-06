const path = require('path')
const merge = require('webpack-merge');
const common = require('./webpack.config.js');

const publicPathURL = process.env.STATIC_URL || '/static/';

module.exports = merge(common, {
  mode: 'production',
  output: {
    path: path.resolve(__dirname, 'templates/dist'),
    filename: '[name].chunkhash.bundle.js',
    chunkFilename: '[name].chunkhash.bundle.js',
    publicPath: publicPathURL
  },
  devtool: '',
  optimization: {
    splitChunks: {
      cacheGroups: {
        vendor: {
          chunks: 'initial',
          name: 'vendor',
          test: '/node_modules/',
          enforce: true
        },
      }
    }
  }
});