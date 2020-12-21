<?php
/**
 * The sidebar containing the main widget area
 *
 * @link https://developer.wordpress.org/themes/basics/template-files/#template-partials
 *
 * @package PopularFX
 */

// If no widgets in sidebar
if ( ! is_active_sidebar( 'sidebar-1' ) ) {
	return;
}

$enabled = NULL;

// For page
if(is_page()){
	$enabled = get_theme_mod('popularfx_sidebar_page', 'default');
}

// For post
if(is_single()){
	$enabled = get_theme_mod('popularfx_sidebar_post', 'right');
}

// For Archives
if(is_archive() || is_home()){
	$enabled = get_theme_mod('popularfx_sidebar_archives', 'right');
}

// Load the default
if($enabled == 'default' || is_front_page()){
	$enabled = get_theme_mod('popularfx_sidebar_default', '0');
}

// If its disabled
if(empty($enabled)){
	return;
}

$width = (int) get_theme_mod('popularfx_sidebar_width', 20);

?>

<style>
aside {
width: <?php echo $width;?>%;
float: <?php echo $enabled;?>;
}

main, .pagelayer-content{
width: <?php echo round(99 - $width);?>% !important;
display: inline-block;
}
</style>

<aside id="secondary" class="widget-area">
	<?php dynamic_sidebar( 'sidebar-1' ); ?>
</aside><!-- #secondary -->