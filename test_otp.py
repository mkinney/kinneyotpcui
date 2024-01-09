from otp import Form

import asyncio

import pytest

@pytest.mark.asyncio
async def test_encode():
    """Test encode works as expected"""
    app = Form()
    async with app.run_test() as pilot:
        await pilot.press("tab", "A", "P", "P", "L", "E", "tab", "H", "E", "L", "L", "O")
        encoded_input = pilot.app.query_one("#encoded")
        assert encoded_input.value == "HTAWS"

@pytest.mark.asyncio
async def test_decode():
    """Test decode works as expected"""
    app = Form()
    async with app.run_test() as pilot:
        await pilot.press("2", "tab", "H", "T", "A", "W", "S", "tab", "H", "E", "L", "L", "O")
        decoded_input = pilot.app.query_one("#decoded")
        assert decoded_input.value == "APPLE"

@pytest.mark.asyncio
async def test_generate():
    """Test generate works as expected"""
    app = Form()
    async with app.run_test() as pilot:
        await pilot.press("3", "tab", "s", "o", "m", "e", " ", "s", "e", "e", "d", " ", "1", "2", "3")
        generated_input = pilot.app.query_one("#generated")
        assert "VFQHA VHXPF ZSJZM OJXFN ZKNDA" in generated_input.text
        assert "HGOWL KOVJY LAGVT PCJZZ VAQVN" in generated_input.text

@pytest.mark.asyncio
async def test_settings():
    """Test settings works as expected"""
    app = Form()
    async with app.run_test() as pilot:
        await pilot.press("4")
        alphabet_input = pilot.app.query_one("#alphabet")
        assert "ABCDEFGHIJKLMNOPQRSTUVWXYZ" in alphabet_input.value
