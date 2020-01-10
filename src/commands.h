/*
 * Copyright (C) 2007-2008, Intel Corp. All rights reserved.
 *
 *
 * This program is free software; you can redistribute it and/or modify it under
 * the terms of the GNU General Public License as published by the Free Software
 * Foundation; either version 2 of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
 * FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License 
 * for more details.
 *
 * You should have received a copy of the GNU General Public License along
 * with this program; if not, write to the Free Software Foundation, Inc.,
 * 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
 */

/*
 * Intel SGPIO enclosure management utility
 * Author: Eric R Hall <Eric.R.Hall@intel.com> 
 * 
 */

struct action_flags {
    char disk[4];
    char state[10];
};

/* command line parsing structs; uses getopt.h */
static int verbose_flag;

/* Setup the commands structure */
static struct option long_options[] = {
    {"verbose",       no_argument, &verbose_flag,   1},
    {"port",    required_argument,             0, 'p'},
    {"disk",    required_argument,             0, 'd'},
    {"status",  required_argument,             0, 's'},
    {"freq",	required_argument,             0, 'f'},
    {"help",          no_argument,             0, 'h'},
    {"version",       no_argument,             0, 'V'},
    {0,                         0,             0,   0}
};

/* Set up the short commands */
static char const *short_options = "p:d:s:" "f:" "h" "V";
