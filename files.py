from enum import Enum
import os

class Files (Enum):
    Img = ["arw", "btf", "tiff", "tif", "cr2", "dcr", "erf", "3fr", "kdc", "k25", "mos", "nef", "mef", "orf", "raw", "rw2", "pef", "srf", "sr2", "svg", "svgz", "shape", "rhif", "ani", "png", "mng", "jxl", "ora", "xjt", "xktgz", "xjtbz2", "sfw", "pwp", "cam", "jpg", "gpe", "jpeg", "j6i", "kqp", "pmp", "img", "iff", "anim", "ilbm", "lbm", "bpg", "dng", "gif", "webp" , "wbmp", "wbm", "wbp"]
    Vid = ["3g2", "3gp", "amv", "asf", "avi", "drc", "flv", "f4v", "f4p", "f4a", "f4b", "gifv", "m4v", "mkv", "mng", "mov", "qt", "mp4", "m4p", "m4v", "mpg", "mp2", "mpeg", "mpe", "mpv", "m2v", "MTS", "M2TS", "TS", "mxf", "nsv", "ogv", "ogg", "rm", "rmvb", "roq", "svi", "vlv", "vob", "webm", "wmv", "yuv"]
    Mus = ["3gp", "aa", "aac", "aax", "act", "aiff", "alac", "amr", "ape", "au", "awb", "dss", "dvf", "flac", "gsm", "iklax", "ivs", "m4a", "m4b", "m4p", "mmf", "mp3", "mpc", "msv", "nmf", "ogg", "oga", "mogg", "opus", "ra", "rm", "raw", "rf64", "sln", "tta", "voc", "vox", "wav", "wma", "wv", "webm", "cda"]
    Doc = ["doc", "pdf", "txt", "rtf", "cwk", "dbk", "dita", "docm", "docx", "dot", "dotx", "dwd", "egt", "epub", "html", "pages", "sdw", "se", "stw", "sxw", "wpd", "wps", "wpt", "wrd", "wrf", "wri", "xhtml", "xps", "md", "fdx", "lwp", "mbp", "mcw", "mobi", "nb", "nbp", "odm", "odoc", "odt", "osheet", "ott", "xps", "djvu", "epub", "fb2", "mobi", "lit", "pptx", "ppt", "xlsx"] 
    Arc = ["zip", "7z", "rar", "tar", "iso", "bz2", "s7z", "apk", "jar", "tbz2", "tlz", "txz", "zipx", "img", "deb", "pkg", "mpkg", "rpm", "tgz", "crx"] 
    App = ["exe", "msi", "sh", "bat"]
    
class File:
    def SearchFile(file):
        for i in Files:
            for j in i.value:
                if (file == j):
                    print(file+" "+i.name)
                    break
            if(Files.App == i):
                print(file+" Oth")

File.SearchFile("iso")
