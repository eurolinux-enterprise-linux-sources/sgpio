########################################################################
# Copyright (C) 2007-2008, Intel Corp. All rights reserved.
#
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License 
# for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
########################################################################


# Intel SGPIO enclosure management utility
#
# Author: Eric R Hall <Eric.R.Hall@intel.com>


MANDIR ?= /usr/local/man
ALL = sgpio

all: $(ALL)

sgpio.o: sgpio.c
	gcc -g -Wall -c sgpio.c

sgpio: sgpio.o
	gcc -g sgpio.o -o sgpio

clean:
	rm -f sgpio.o sgpio

install: $(ALL)
	for i in $(ALL); do \
		install $$i /sbin/$$i; \
	done
	install -d $(MANDIR)/man1
	install -m 0644 *.1 $(MANDIR)/man1

uninstall:
	for i in $(ALL); do \
		rm -f /sbin/$$i; \
	done
	for i in $(ALL:=.1); do \
		rm -f $(MANDIR)/man1/$$i; \
	done
