"""
==========================================================
Bangladesh Result Hub (BRH)

Education Board Mapper

Version : 1.0.0
==========================================================
"""

from __future__ import annotations

BOARD_MAP = {

    # Dhaka
    "DHAKA": "DHAKA",
    "Dhaka": "DHAKA",
    "dhaka": "DHAKA",
    "ঢাকা": "DHAKA",

    # Rajshahi
    "RAJSHAHI": "RAJSHAHI",
    "Rajshahi": "RAJSHAHI",
    "rajshahi": "RAJSHAHI",
    "রাজশাহী": "RAJSHAHI",

    # Jessore
    "JESSORE": "JESSORE",
    "Jessore": "JESSORE",
    "jessore": "JESSORE",
    "Jashore": "JESSORE",
    "যশোর": "JESSORE",

    # Khulna
    "KHULNA": "KHULNA",
    "Khulna": "KHULNA",
    "khulna": "KHULNA",
    "খুলনা": "KHULNA",

    # Chittagong
    "CHITTAGONG": "CHITTAGONG",
    "Chittagong": "CHITTAGONG",
    "chittagong": "CHITTAGONG",
    "চট্টগ্রাম": "CHITTAGONG",

    # Comilla
    "COMILLA": "COMILLA",
    "Comilla": "COMILLA",
    "comilla": "COMILLA",
    "কুমিল্লা": "COMILLA",
    "Cumilla": "COMILLA",
    "cumilla": "COMILLA",
    
    # Barisal
    "BARISAL": "BARISAL",
    "Barisal": "BARISAL",
    "barisal": "BARISAL",
    "বরিশাল": "BARISAL",

    # Sylhet
    "SYLHET": "SYLHET",
    "Sylhet": "SYLHET",
    "sylhet": "SYLHET",
    "সিলেট": "SYLHET",

    # Dinajpur
    "DINAJPUR": "DINAJPUR",
    "Dinajpur": "DINAJPUR",
    "dinajpur": "DINAJPUR",
    "দিনাজপুর": "DINAJPUR",

    # Mymensingh
    "MYMENSINGH": "MYMENSINGH",
    "Mymensingh": "MYMENSINGH",
    "mymensingh": "MYMENSINGH",
    "ময়মনসিংহ": "MYMENSINGH",

    # Madrasa
    "MADRASA": "MADRASA",
    "Madrasa": "MADRASA",
    "madrasa": "MADRASA",
    "মাদ্রাসা": "MADRASA",

    # Technical
    "TECHNICAL": "TECHNICAL",
    "Technical": "TECHNICAL",
    "technical": "TECHNICAL",
    "কারিগরি": "TECHNICAL",
}

def normalize_board(board: str) -> str:
    """
    Convert any board name into BRH standard format.
    """

    if board is None:
        return ""

    board = " ".join(str(board).split())

    return BOARD_MAP.get(board, board.upper())


def is_supported_board(board: str) -> bool:
    """
    Check board support.
    """

    return normalize_board(board) in {
        "DHAKA",
        "RAJSHAHI",
        "JESSORE",
        "KHULNA",
        "CHITTAGONG",
        "COMILLA",
        "BARISAL",
        "SYLHET",
        "DINAJPUR",
        "MYMENSINGH",
        "MADRASA",
        "TECHNICAL",
    }


def get_all_boards() -> list[str]:
    """
    Return supported board list.
    """

    return [
        "DHAKA",
        "RAJSHAHI",
        "JESSORE",
        "KHULNA",
        "CHITTAGONG",
        "COMILLA",
        "BARISAL",
        "SYLHET",
        "DINAJPUR",
        "MYMENSINGH",
        "MADRASA",
        "TECHNICAL",
    ]


def display_name(board: str) -> str:
    """
    User friendly board name.
    """

    board = normalize_board(board)

    names = {
        "DHAKA": "Dhaka",
        "RAJSHAHI": "Rajshahi",
        "JESSORE": "Jessore",
        "KHULNA": "Khulna",
        "CHITTAGONG": "Chittagong",
        "COMILLA": "Comilla",
        "BARISAL": "Barisal",
        "SYLHET": "Sylhet",
        "DINAJPUR": "Dinajpur",
        "MYMENSINGH": "Mymensingh",
        "MADRASA": "Madrasa",
        "TECHNICAL": "Technical",
    }

    return names.get(board, board.title())
