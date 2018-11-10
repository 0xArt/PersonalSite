/**
 * @license Copyright (c) 2003-2018, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see https://ckeditor.com/legal/ckeditor-oss-license
 */

CKEDITOR.editorConfig = function( config ) {
	// Define changes to default configuration here. For example:
	// config.language = 'fr';
	// config.uiColor = '#AADC6E';
	config.allowedContent = true;
};

// If you want inserted images in a CKEditor to be responsive
// you can use the following code. It creates a htmlfilter for the
// image tag that replaces inline "width" and "style" definitions with
// their corresponding attributes and add's (in this example) the
// Bootstrap "img-responsive" class.
