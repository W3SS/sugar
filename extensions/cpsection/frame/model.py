# Copyright (C) 2008 One Laptop Per Child
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#

from jarabe.frame import get_view

frame = get_view()


def get_corner_delay():
    corner_delay = frame.settings.get_int('corner-delay')
    return corner_delay


def print_corner_delay():
    print get_corner_delay()


def set_corner_delay(delay):
    """Set a delay for the activation of the frame using hot corners.
    instantaneous: 0 (0 milliseconds)
    delay: 100 (100 milliseconds)
    never: 1000 (disable activation)
    """
    frame.settings.set_int('corner-delay', int(delay))
    return 0


def get_edge_delay():
    edge_delay = frame.settings.get_int('edge-delay')
    return edge_delay


def print_edge_delay():
    print get_edge_delay()


def set_edge_delay(delay):
    """Set a delay for the activation of the frame using warm edges.
    instantaneous: 0 (0 milliseconds)
    delay: 100 (100 milliseconds)
    never: 1000 (disable activation)
    """
    frame.settings.set_int('edge-delay', int(delay))
    return 0


def get_trigger_size():
    trigger_size = frame.settings.get_int('trigger-size')
    return trigger_size


def print_trigger_size():
    print '{}px'.format(get_trigger_size())


def set_trigger_size(size):
    """
    Set the size of the frame trigger area, in px from the corner/edge.

    exactly on the edge: 1
    """
    frame.settings.set_int('trigger-size', int(size))
    return 0
