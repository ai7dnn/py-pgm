while True:
    print("\n=== 메뉴 화면 ===")
    print("  메뉴1 (1)")
    print("  메뉴2 (2)")
    print("  종 료 (q)\n")
    ch = input("메뉴를 선택하세요(1, 2, q): ")
    if ch=='1' :
        print("메뉴1을 선택했습니다!")
        input("[<enter> 키 입력]")
    elif ch=='2' :
        print("메뉴2를 선택했습니다!")
        input("[<enter> 키 입력]")
    elif ch=='q' :
        break   # 메뉴 화면 종료
    else  : 
        print("1, 2, q를 선택해야 합니다. 다시 선택해 주세요!")
print("메뉴 화면을 종료합니다!")
