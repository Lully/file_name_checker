# coding: utf-8

import os
from stdf import create_file

liste = [
"gme-10025-000_0.jpg",
"gme-10026-000_0.jpg",
"gme-10170-001_0.jpg",
"gme-10314-003_0.jpg",
"gme-10437-000_0.jpg",
"gme-11010-000_0.jpg",
"gme-11571-000_0.jpg",
"gme-11817-000_0.jpg",
"gme-11616-000_1725.jpg",
"gme-11748-000_1719.jpg",
"gme-12544-000_1712.jpg",
"gme-12545-000_1715.jpg",
"gme-12546-000_1720.jpg",
"gme-12547-000_1711.jpg",
"gme-5313-000_1727.jpg",
"gme-7077-000_1707.jpg",
"gme-7996-000_1706.jpg",
"gml-5446-000_1720.jpg",
"gml-6536-001_1722.jpg",
"gml-7723-000_1716.jpg",
"gmlc-723-001_1721.jpg",
"gmt-11162-002_1699.jpg",
"gmt-18189-000_1698.jpg",
"gmt-18842-001_1713.jpg",
"gmt-19615-003_1697.jpg",
"gmt-24806-001_1718.jpg",
"gmt-25521-000_1702.jpg",
"gmt-26627-019_1704.jpg",
"gmt-26631-002_1705.jpg",
"gmt-26637-077_1723.jpg",
"gmt-26637-083_1708.jpg",
"gmt-27015-007_1709.jpg",
"gmt-27578-013_1723.jpg",
"gmt-28575-000_1726.jpg",
"gmt-30821-001_1709.jpg",
"gmt-30821-002_1703.jpg",
"gmt-30821-003_1709.jpg",
"gmt-30821-004_1709.jpg",
"gmt-30821-012_1703.jpg",
"gmt-30821-014_1708.jpg",
"gmt-30821-023_1708.jpg",
"gmt-7766-002_1700.jpg",
"c-138-000_63 2003.jpg",
"gme-11015-000_109 2003.jpg",
"gme-12308-001_203 2003.jpg",
"gme-13052-000_259 2003.jpg",
"gme-13087-002_192 2003.jpg",
"gme-13272-000_137.jpg"
]


for el in liste:
    output_filepath = os.path.join(r"tests", el)
    create_file(output_filepath)
    