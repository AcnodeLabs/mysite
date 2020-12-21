<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'acnodela_wp853' );

/** MySQL database username */
define( 'DB_USER', 'acnodela_wp853' );

/** MySQL database password */
define( 'DB_PASSWORD', '[7S)6Y5Jb[@p1SN.' );

/** MySQL hostname */
define( 'DB_HOST', 'localhost' );

/** Database Charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The Database Collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         'vxvf9ugdvzeo1rgcjckzht0trgbqqtqnpwakpdxkfocpujixox0pxuufstxfqrf8' );
define( 'SECURE_AUTH_KEY',  'g9qdkdilgkjqqa57597baxhbattlmm3yieajmz5jrhdffvmkjdthhptfskpjbyhd' );
define( 'LOGGED_IN_KEY',    'ykbxclmd8jsfheku8lk9tonejvz2vy4cyeb1nuwloe4wilmqh5iirinzrhugnoo0' );
define( 'NONCE_KEY',        'e17itli70y9hyiwopiw81sfr4swsitfg6tc1lwyndkm1up8ahwsq9tb89hw4uafx' );
define( 'AUTH_SALT',        'cli8gufecfcuyofxxjv5sjnkgxanzpfntwnkzv7c6ad41enrmkpctdofj8ur8kmh' );
define( 'SECURE_AUTH_SALT', 'x8dly3ccxe30flgurq9zvyteefcju7zdy5ibwjjeyqwztopscymor843xpwltn27' );
define( 'LOGGED_IN_SALT',   'lkxr7pebwesaof20kxmhzozq0aeo84bpiqgyiijvwbqtoa7fikojmw9eftjnbm1p' );
define( 'NONCE_SALT',       'matv7ofzcd8aeexxicjxetwlodb8uaxgvczbdqdrvokwy7ldayrzapmyaadz6b25' );

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wpnh_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/support/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', false );

/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
