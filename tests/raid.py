def main(namespace, src):
    func = namespace["main"]
    bfck0 = "--[----->+<]>---.++++++++++++.+.+++++++++.+[-->+<]>+++.++[-->+++<]>.++++++++++++.+.+++++++++.-[-->+++++<]>++.[--->++<]>-.-----------."
    bfck1 = ">++++++++[<++++++++>-]<.>++++[<+++++++>-]<+.+++++++..+++.>>++++++[<+++++++>-]<++.------------.>++++++[<+++++++++>-]<+.<.+++.-----.--------.>>>++++[<+++++++>-]<+."
    res0 = "copy@copy.sh"
    res1 = "@]ddg, Wgje]"
    for bfck, res in ((bfck0, res0), (bfck1, res1)):
        try:
            result = func(bfck)
            if result == res:
                error_code, message = 0, "Bravo !"
            else:
                error_code, message = 1, ""
                break
        except Exception as e:
            error_code, message = 1, str(e)
    return error_code, message
