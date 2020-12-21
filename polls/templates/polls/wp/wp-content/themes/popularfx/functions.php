<?php
/**
 * PopularFX functions and definitions
 *
 * @link https://popularfx.com/docs/
 *
 * @package PopularFX
 */

if ( ! defined( 'POPULARFX_VERSION' ) ) {
	// Replace the version number of the theme on each release.
	define( 'POPULARFX_VERSION', '1.0.5' );
}

if ( ! defined( 'POPULARFX_PAGELAYER_API' ) ) {
	define( 'POPULARFX_PAGELAYER_API', 'https://api.pagelayer.com/' );
}

if ( ! defined( 'POPULARFX_WWW_URL' ) ) {
	define( 'POPULARFX_WWW_URL', 'https://popularfx.com' );
}

if ( ! defined( 'POPULARFX_PRO_URL' ) ) {
	define( 'POPULARFX_PRO_URL', 'https://popularfx.com/pricing?from=pfx-theme' );
}

if ( ! defined( 'POPULARFX_URL' ) ) {
	define( 'POPULARFX_URL', get_template_directory_uri() );
}

if(!defined('PAGELAYER_VERSION')){
	define('POPULARFX_PAGELAYER_PRO_URL', 'https://pagelayer.com/pricing?from=pfx-theme');
}

if ( ! function_exists( 'popularfx_setup' ) ){
	/**
	 * Sets up theme defaults and registers support for various WordPress features.
	 *
	 * Note that this function is hooked into the after_setup_theme hook, which
	 * runs before the init hook. The init hook is too late for some features, such
	 * as indicating support for post thumbnails.
	 */
	function popularfx_setup() {
		/*
		 * Make theme available for translation.
		 * Translations can be filed in the /languages/ directory.
		 * If you're building a theme based on PopularFX, use a find and replace
		 * to change 'popularfx' to the name of your theme in all the template files.
		 */
		load_theme_textdomain( 'popularfx', get_stylesheet_directory() . '/languages' );

		// Add default posts and comments RSS feed links to head.
		add_theme_support( 'automatic-feed-links' );

		/*
		 * Let WordPress manage the document title.
		 * By adding theme support, we declare that this theme does not use a
		 * hard-coded <title> tag in the document head, and expect WordPress to
		 * provide it for us.
		 */
		add_theme_support( 'title-tag' );

		/*
		 * Enable support for Post Thumbnails on posts and pages.
		 *
		 * @link https://developer.wordpress.org/themes/functionality/featured-images-post-thumbnails/
		 */
		add_theme_support( 'post-thumbnails' );

		// This theme uses wp_nav_menu() in two locations.
		register_nav_menus(
			array(
				'primary' => __( 'Primary Menu', 'popularfx' ),
			)
		);

		/*
		 * Switch default core markup for search form, comment form, and comments
		 * to output valid HTML5.
		 */
		add_theme_support(
			'html5',
			array(
				'search-form',
				'comment-form',
				'comment-list',
				'gallery',
				'caption',
				'style',
				'script',
			)
		);

		// Add theme support for selective refresh for widgets.
		add_theme_support( 'customize-selective-refresh-widgets' );

		/**
		 * Add support for core custom logo.
		 *
		 * @link https://codex.wordpress.org/Theme_Logo
		 */
		add_theme_support(
			'custom-logo',
			array(
				'height'      => 250,
				'width'       => 250,
				'flex-width'  => true,
				'flex-height' => true,
			)
		);
		
		global $pagelayer, $popularfx;
		if(!empty($pagelayer->settings)){
			$pagelayer->template_call_sidebar = 1;
		}
		
		// Force copyright for the free version
		if(!defined('PFX_VERSION')){
			$copyright = get_option('pagelayer-copyright');
			if(empty($popularfx['license']['status']) && empty($pagelayer->license['status']) && !preg_match('/popularfx/is', $copyright)){
				update_option('pagelayer-copyright', popularfx_copyright());
			}
		}
		
		// Show promos
		popularfx_promos();
		
		$template = get_theme_mod('popularfx_template');
		if(empty($template)){
		
			// Set up the WordPress core custom background feature.
			add_theme_support('custom-background',
				apply_filters(
					'popularfx_custom_background_args',
					array(
						'default-color' => 'ffffff',
						'default-image' => '',
					)
				)
			);
			
			add_theme_support( 'custom-header',
				apply_filters(
					'popularfx_custom_header_args',
					array(
						'default-image'      => '',
						'default-text-color' => '000000',
						'width'              => 1000,
						'height'             => 250,
						'flex-height'        => true,
						'wp-head-callback'   => 'popularfx_header_style',
					)
				)
			);
		
		}
		
	}
}
add_action( 'after_setup_theme', 'popularfx_setup' );

/**
 * Set the content width in pixels, based on the theme's design and stylesheet.
 *
 * Priority 0 to make it available to lower priority callbacks.
 *
 * @global int $content_width
 */
function popularfx_content_width() {
	// This variable is intended to be overruled from themes.
	// Open WPCS issue: {@link https://github.com/WordPress-Coding-Standards/WordPress-Coding-Standards/issues/1043}.
	// phpcs:ignore WordPress.NamingConventions.PrefixAllGlobals.NonPrefixedVariableFound
	$GLOBALS['content_width'] = apply_filters( 'popularfx_content_width', 640 );
}

function popularfx_copyright(){
	return '<a href="'.POPULARFX_WWW_URL.'">PopularFX Theme</a>';
}

// Shows the promos
function popularfx_promos(){
	
	if(is_admin() && current_user_can('install_themes')){
	
		// Show the promo
		popularfx_maybe_promo([
			'after' => 1,// In days
			'interval' => 30,// In days
			'pro_url' => POPULARFX_PRO_URL,
			'rating' => 'https://wordpress.org/themes/popularfx/#reviews',
			'twitter' => 'https://twitter.com/PopularFXthemes?status='.rawurlencode('I love #PopularFX Theme by @pagelayer team for my #WordPress site - '.home_url()),
			'facebook' => 'https://facebook.com/popularfx',
			'website' => POPULARFX_WWW_URL,
			'image' => POPULARFX_URL.'/images/popularfx-logo.png',
			'name' => 'popularfx_show_promo'
		]);
		
		$template = get_theme_mod('popularfx_template');
		if(empty($template)){
		
			// Show the image promo
			popularfx_maybe_promo([
				'after' => 0,// In days
				'interval' => 30,// In days
				'pro_url' => POPULARFX_PRO_URL,
				'rating' => 'https://wordpress.org/themes/popularfx/#reviews',
				'twitter' => 'https://twitter.com/PopularFXthemes?status='.rawurlencode('I love #PopularFX Theme by @pagelayer team for my #WordPress site - '.home_url()),
				'facebook' => 'https://facebook.com/popularfx',
				'website' => POPULARFX_WWW_URL,
				'image' => POPULARFX_URL.'/images/popularfx-logo.png',
				'name' => 'popularfx_templates_promo'
			]);
		
		}
		//delete_option('popularfx_templates_promo');
	
	}
	
}
add_action( 'after_switch_theme', 'popularfx_promos', 10 );

/**
 * Register widget area.
 *
 * @link https://developer.wordpress.org/themes/functionality/sidebars/#registering-a-sidebar
 */
function popularfx_widgets_init() {
	register_sidebar(
		array(
			'name'          => esc_html__( 'Sidebar', 'popularfx' ),
			'id'            => 'sidebar-1',
			'description'   => esc_html__( 'Add widgets here.', 'popularfx' ),
			'before_widget' => '<section id="%1$s" class="widget %2$s">',
			'after_widget'  => '</section>',
			'before_title'  => '<h2 class="widget-title">',
			'after_title'   => '</h2>',
		)
	);
}
add_action( 'widgets_init', 'popularfx_widgets_init' );

/**
 * Enqueue scripts and styles.
 */
function popularfx_scripts() {
	
	$template = get_theme_mod('popularfx_template');
	if(!empty($template)){
		wp_enqueue_style( 'popularfx-style', get_stylesheet_directory_uri().'/templates/'.$template.'/style.css', array(), POPULARFX_VERSION );
		wp_enqueue_style( 'popularfx-sidebar', get_stylesheet_directory_uri().'/sidebar.css', array(), POPULARFX_VERSION );
	}else{
		wp_enqueue_style( 'popularfx-style', get_stylesheet_uri(), array(), POPULARFX_VERSION );
		wp_style_add_data( 'popularfx-style', 'rtl', 'replace' );
	}	

	wp_enqueue_script( 'popularfx-navigation', get_stylesheet_directory_uri() . '/js/navigation.js', array(), POPULARFX_VERSION, true );

	if ( is_singular() && comments_open() && get_option( 'thread_comments' ) ) {
		wp_enqueue_script( 'comment-reply' );
	}
}
add_action( 'wp_enqueue_scripts', 'popularfx_scripts' );

function popularfx_the_title($before = '', $after = '', $echo = true){
	if(is_page()){
		return;
	}
	
	the_title($before, $after, $echo);
}

// Show the templates promo
function popularfx_templates_promo(){
	
	global $popularfx_promo_opts, $popularfx;
	
	$opts = $popularfx_promo_opts['popularfx_templates_promo'];
	
	echo '<style>
#popularfx_templates_promo{
border-left: 1px solid #ccd0d4;
}

.popularfx-templates-promo{
background: #fff;
padding: 5px;
}

.popularfx_promo_button {
background-color: #4CAF50; /* Green */
border: none;
color: white;
padding: 6px 10px;
text-align: center;
text-decoration: none;
display: inline-block;
font-size: 13px;
margin: 4px 2px;
-webkit-transition-duration: 0.4s; /* Safari */
transition-duration: 0.4s;
cursor: pointer;
}
.popularfx_promo_button:focus,
.popularfx_promo_button:hover{
border: none;
color: white;
box-shadow: 0 6px 8px 0 rgba(0,0,0,0.24), 0 9px 25px 0 rgba(0,0,0,0.19);
color: white;
}
.popularfx_promo_buy {
color: white;
padding: 8px 12px;
font-size: 14px;
}
.popularfx_promo_button1 {
color: white;
background-color: #4CAF50;
border:3px solid #4CAF50;
}
.popularfx_promo_button1:hover {
border:3px solid #4CAF50;
}
.popularfx_promo_button2 {
color: white;
background-color: #0085ba;
}
.popularfx_promo_button3 {
color: white;
background-color: #365899;
}
.popularfx_promo_button4 {
color: white;
background-color: rgb(66, 184, 221);
}
.popularfx_promo-close{
float:right;
text-decoration:none;
margin: 5px 10px 0px 0px;
}
.popularfx_promo-close:hover{
color: red;
}
}

</style>
<script type="application/javascript">
	jQuery(document).ready(function(){
		jQuery("#popularfx_templates_promo .popularfx_promo-close").click(function(){
			var data;
			jQuery("#popularfx_templates_promo").hide();
			// Save this preference
			jQuery.post("'.admin_url('?'.$opts['name'].'=0').'", data, function(response) {
				//alert(response);
			});
		});
	});
</script>

	<div class="'.(empty($opts['class']) ? 'notice notice-success' : 'popularfx-templates-promo').'" id="popularfx_templates_promo" style="min-height:90px">
		<a class="popularfx_promo-close" href="javascript:" aria-label="Dismiss this Notice">
			<span class="dashicons dashicons-dismiss"></span> Dismiss
		</a>
		<center style="margin:10px;">
			<a href="'.POPULARFX_WWW_URL.'/templates" style="text-decoration: none; font-size: 15px;">
				Did you know PopularFX comes with 500+ Templates to design your website. Click to choose your template !<br>
				<img src="'.POPULARFX_URL.'/images/templates.jpg" width="40%" />
			</a>
		</center>
		<div class="popularfx_promo-left">
			<p align="center">
				'.(empty($opts['pro_url']) || !empty($popularfx['license']) ? '' : '<a class="popularfx_promo_button popularfx_promo_buy" target="_blank" href="'.$opts['pro_url'].'">Buy PopularFX Pro</a>').'
				'.(empty($opts['rating']) ? '' : '<a class="popularfx_promo_button popularfx_promo_button2" target="_blank" href="'.$opts['rating'].'">Rate it 5★\'s</a>').'
				'.(empty($opts['facebook']) ? '' : '<a class="popularfx_promo_button popularfx_promo_button3" target="_blank" href="'.$opts['facebook'].'"><span class="dashicons dashicons-thumbs-up"></span> Facebook</a>').'
				'.(empty($opts['twitter']) ? '' : '<a class="popularfx_promo_button popularfx_promo_button4" target="_blank" href="'.$opts['twitter'].'"><span class="dashicons dashicons-twitter"></span> Tweet</a>').'
				'.(empty($opts['website']) ? '' : '<a class="popularfx_promo_button popularfx_promo_button4" target="_blank" href="'.$opts['website'].'">Visit our website</a>').'
			</p>
		</div>
	</div>';
	
}

// Show promo notice on dashboard
function popularfx_show_promo($opts = []){
	
	global $popularfx_promo_opts, $popularfx;

	$opts = $popularfx_promo_opts['popularfx_show_promo'];
	
	echo '<style>
#popularfx_promo{
border-left: 1px solid #ccd0d4;
}

.popularfx_promo_button {
background-color: #4CAF50; /* Green */
border: none;
color: white;
padding: 6px 10px;
text-align: center;
text-decoration: none;
display: inline-block;
font-size: 13px;
margin: 4px 2px;
-webkit-transition-duration: 0.4s; /* Safari */
transition-duration: 0.4s;
cursor: pointer;
}
.popularfx_promo_button:focus,
.popularfx_promo_button:hover{
border: none;
color: white;
box-shadow: 0 6px 8px 0 rgba(0,0,0,0.24), 0 9px 25px 0 rgba(0,0,0,0.19);
color: white;
}
.popularfx_promo_buy {
color: white;
padding: 8px 12px;
font-size: 14px;
}
.popularfx_promo_button1 {
color: white;
background-color: #4CAF50;
border:3px solid #4CAF50;
}
.popularfx_promo_button1:hover {
border:3px solid #4CAF50;
}
.popularfx_promo_button2 {
color: white;
background-color: #0085ba;
}
.popularfx_promo_button3 {
color: white;
background-color: #365899;
}
.popularfx_promo_button4 {
color: white;
background-color: rgb(66, 184, 221);
}
.popularfx_promo-close{
float:right;
text-decoration:none;
margin: 5px 10px 0px 0px;
}
.popularfx_promo-close:hover{
color: red;
}

.popularfx_promo-left{
display: inline-block; width: 65%; vertical-align: top;
}

.popularfx_promo-right{
display: inline-block; width: 35%; vertical-align: top
}

@media all and (max-width:599px){
.popularfx_promo-left, .popularfx_promo-right{
width: 100%;
}
}

</style>
<script type="application/javascript">
	jQuery(document).ready(function(){
		jQuery("#popularfx_promo .popularfx_promo-close").click(function(){
			var data;
			jQuery("#popularfx_promo").hide();
			// Save this preference
			jQuery.post("'.admin_url('?'.$opts['name'].'=0').'", data, function(response) {
				//alert(response);
			});
		});
	});
</script>

	<div class="notice notice-success" id="popularfx_promo" style="min-height:90px">
		<div class="popularfx_promo-left">';
	
	if(!empty($opts['image'])){
		echo '<a href="'.$opts['website'].'"><img src="'.$opts['image'].'" style="float:left; margin:25px 20px 10px 10px" width="67" /></a>';
	}
	
	echo '
		<p style="font-size:14px; line-height: 1.6">We are glad you are using <a href="'.$opts['website'].'"><b>PopularFX</b></a> to build your website. We really appreciate it ! <br>We would like to request you to give us a 5 Star rating on <a href="'.$opts['rating'].'" target="_blank">WordPress.org</a>. <br>It will greatly boost our motivation !</p>
		<p>
			'.(empty($opts['pro_url']) || !empty($popularfx['license']) ? '' : '<a class="popularfx_promo_button popularfx_promo_buy" target="_blank" href="'.$opts['pro_url'].'">Buy PopularFX Pro</a>').'
			'.(empty($opts['rating']) ? '' : '<a class="popularfx_promo_button popularfx_promo_button2" target="_blank" href="'.$opts['rating'].'">Rate it 5★\'s</a>').'
			'.(empty($opts['facebook']) ? '' : '<a class="popularfx_promo_button popularfx_promo_button3" target="_blank" href="'.$opts['facebook'].'"><span class="dashicons dashicons-thumbs-up"></span> Facebook</a>').'
			'.(empty($opts['twitter']) ? '' : '<a class="popularfx_promo_button popularfx_promo_button4" target="_blank" href="'.$opts['twitter'].'"><span class="dashicons dashicons-twitter"></span> Tweet</a>').'
			'.(empty($opts['website']) ? '' : '<a class="popularfx_promo_button popularfx_promo_button4" target="_blank" href="'.$opts['website'].'">Visit our website</a>').'
		</p>
		'.(empty($opts['pro_url']) || !empty($popularfx['license']) ? '' : '<p style="font-size:13px"><a href="'.$opts['pro_url'].'"><b>PopularFX Pro</b></a> has many more features like 500+ <a href="'.$opts['website'].'/templates">Website Templates</a>, 90+ widgets, 500+ sections, Theme Builder, WooCommerce Builder, Theme Creator and Exporter, Form Builder, Popup Builder, etc. You get a Pagelayer Pro license with the PopularFX Pro version.
		</p>').'
		</div>';
	

	
	echo '<div class="popularfx_promo-right">
			<a class="popularfx_promo-close" href="javascript:" aria-label="Dismiss this Notice">
				<span class="dashicons dashicons-dismiss"></span> Dismiss
			</a>
			<br>
			<center style="margin:10px;">
				<a href="'.POPULARFX_WWW_URL.'/templates" style="text-decoration: none; font-size: 15px;"><img src="'.POPULARFX_URL.'/images/templates.jpg" width="100%" /><br><br>Install from 500+ Website Templates</a>
			</center>
		</div>
	</div>';

}

// Are we to show a promo ?
function popularfx_maybe_promo($opts){
	
	global $popularfx_promo_opts;
	
	// There must be an interval
	if(empty($opts['interval'])){
		return false;
	}
	
	// Are we to show a promo	
	$opt_name = empty($opts['name']) ? 'popularfx_show_promo' : $opts['name'];
	$func = empty($opts['name']) ? $opt_name : $opts['name'];
	$promo_time = get_theme_mod($opt_name);
	//echo $opt_name.' - '.$func.' - '.date('Ymd', $promo_time).'<br>';
	
	// First time access
	if(empty($promo_time)){
		set_theme_mod($opt_name, time() + (!empty($opts['after']) ? $opts['after'] * 86400 : 0));
		$promo_time = get_theme_mod($opt_name);
	}
	
	// Is there interval elapsed
	if(time() >= $promo_time){
		$popularfx_promo_opts[$opt_name] = $opts;
		add_action('admin_notices', $func);
	}
	
	// Are we to disable the promo
	if(isset($_GET[$opt_name]) && (int)$_GET[$opt_name] == 0){
		set_theme_mod($opt_name, time() + ($opts['interval'] * 86400));
		die('DONE');
	}
	
}

// Check if a field is posted via POST else return default value
function popularfx_optpost($name, $default = ''){

	if(!empty($_POST[$name])){
		return popularfx_inputsec(popularfx_htmlizer(trim($_POST[$name])));
	}

	return $default;
}



function popularfx_inputsec($string){

	$string = addslashes($string);

	// This is to replace ` which can cause the command to be executed in exec()
	$string = str_replace('`', '\`', $string);

	return $string;

}

function popularfx_htmlizer($string){

	$string = htmlentities($string, ENT_QUOTES, 'UTF-8');

	preg_match_all('/(&amp;#(\d{1,7}|x[0-9a-fA-F]{1,6});)/', $string, $matches);//r_print($matches);

	foreach($matches[1] as $mk => $mv){
		$tmp_m = popularfx_entity_check($matches[2][$mk]);
		$string = str_replace($matches[1][$mk], $tmp_m, $string);
	}

	return $string;

}

function popularfx_entity_check($string){

	//Convert Hexadecimal to Decimal
	$num = ((substr($string, 0, 1) === 'x') ? hexdec(substr($string, 1)) : (int) $string);

	//Squares and Spaces - return nothing 
	$string = (($num > 0x10FFFF || ($num >= 0xD800 && $num <= 0xDFFF) || $num < 0x20) ? '' : '&#'.$num.';');

	return $string;

}

if ( ! function_exists( 'popularfx_header_style' ) ) :
	/**
	 * Styles the header image and text displayed on the blog.
	 *
	 * @see popularfx_custom_header_setup().
	 */
	function popularfx_header_style() {
		$header_text_color = get_header_textcolor();

		/*
		 * If no custom options for text are set, let's bail.
		 * get_header_textcolor() options: Any hex value, 'blank' to hide text. Default: add_theme_support( 'custom-header' ).
		 */
		if ( get_theme_support( 'custom-header', 'default-text-color' ) === $header_text_color ) {
			return;
		}

		// If we get this far, we have custom styles. Let's do this.
		?>
		<style type="text/css">
		<?php
		// Has the text been hidden?
		if ( ! display_header_text() ) :
			?>
			.site-title,
			.site-description {
				position: absolute;
				clip: rect(1px, 1px, 1px, 1px);
				}
			<?php
			// If the user has set a custom color for the text use that.
		else :
			?>
			.site-title a,
			.site-description {
				color: #<?php echo esc_attr( $header_text_color ); ?>;
			}
		<?php endif; ?>
		</style>
		<?php
	}
endif;

/**
 * Custom template tags for this theme.
 */
require get_stylesheet_directory() . '/inc/template-tags.php';

/**
 * Functions which enhance the theme by hooking into WordPress.
 */
require get_stylesheet_directory() . '/inc/template-functions.php';

/**
 * Customizer additions.
 */
require get_stylesheet_directory() . '/inc/customizer.php';

/**
 * Load WooCommerce compatibility file.
 */
//if ( class_exists( 'WooCommerce' ) ) {
	//require get_stylesheet_directory() . '/inc/woocommerce.php';
//}

// Update the theme
require_once dirname( __FILE__ ) . '/inc/popularfx.php';

