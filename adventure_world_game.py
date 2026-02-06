print("*****************ADVENTURE WORLD****************")
print("Welcome to 'ADVENTURE WORLD GAME'")
print("*************************************************")
name = input("Enter your name here:=> ")
print(f"Hey,{name}")
print(f"{name},Aap ek Adventurer👲 ho OK.")
print("☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠")
print("Game Story:-")
print("             Aapka Adventure ye hai ki aapko sahi raste par jaate jaate 'HIDDEN VILLAGE' ka raste batane wala map ko lana hai..")
print("☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠")

print("Let's Play The Game..😎")
input("Press 'ENTER' to play The Game.")
print("☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠")

print("=>Tum ek sunsan road ke end point par ho, jha do✌ raste hai (left oor right) aap kon sa raste par jana chate ho")
ans1 = input("[Enter (left):for left and (right) : for right]:=> ").lower()

if ans1 == "left":
        print("=>Good, Ye rasta do✌ jagha jata hai (PANDAV VILLAGE OOR BEACH) ap kon se jagha par jana chate ho")
        left_ans1 = input("[Enter Pandav:for PANDAV VILLAGE and Beach:for BEACH]:=> ").lower()
        if left_ans1 =="pandav":
               print("☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠")
               print("Nice Move")
               print("=>Good, Yha per ek 'STRANGER PERSON' hai kya aap usse milana chate ho..?")
               left_ans2 = input("[Type YES :for yes and No :for no]=> ").lower()
               if left_ans2 == "yes" :
                      print("☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠")
                      print("OKAY")
                      print("'Stranger' kheta hai ki use 'Hidden village' ka rasta pata hai")
                      print("Par rasta is 'Paheli' mai chupa hai")
                      print("Paheli:-")
                      print("           Sone ki vo chez hai\n par beche tha nahi hai sunar\n mol tho jada nahi hai uska\n par bhaut hai uska bhaar..  ") 
                    #   ans-charpai -------------------
                      left_ans3 = input("Batau kya hai vo chez :=> ")
                      if left_ans3 == "Charpai":
                             print("☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠")
                             print("Ye sahi jabab hai ")
                             print("But You LOOSE...😥")
                             print("Stranger ne aapke saath majak kiya")
                      else:
                            print("☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠")
                            print("Invalid input😑..Please Play Again")  
               elif left_ans2 =="no":
                            print("You LOOSE..😥")
                            print("Aapko 'Stranger' se baat karni thi")



                      
               elif left_ans1 =="beach":
                            print("☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠")
                            print("You LOOSE..😥")
                            print("This is Wrong Move")
                            print("Beach par Baad aa gayi oor aap mar gye")
               else:
                print("☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠")
                print("Invalid input😑..Please Plya Again") 
elif ans1 == "right":
        print("☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠")
        print("=>Good, Ye rasta ek Jungle mai jata hai, kya aap ishe raste par aage jana chate ho ya  phir Back jana chate")  
        right_ans1 = input("[Enter Go:for GO and Back:for Back]:=> ").lower()
        print("Okay..")
        if right_ans1 == "go":
                print("☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠")
                print("=>Good, Yha per ek 'STRANGER PERSON' hai kya aap usse milana chate ho..?")
                right_ans2 = input("[Type YES :for yes and No :for no]").lower()
                if right_ans2 == "yes":
                       print("☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠")
                       print("OOPS\n You LOOSE.... 'Stranger' ek killer tha aap uske hatho mare gaye..😥")
                elif right_ans2 == "no":
                       print("☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠")
                       print("Nice Move")
                       print(f"=>Accha kar rahe ho {name},Ab jungle mai aage jaate jaaet apko do✌ tunnel melte hai 'Tunnel_1 and tunnel_2'" )
                       print("Aap konsi tunnel mai jaana chate ho..?")
                       right_ans3 = input("[Type 1 :for tunnel_1 and type 2 :for tunnel_2]").lower()
                       if right_ans3 == "1":
                              print("☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠")
                              print("Good")
                              print("=>Tunnel mai jaate jaate apko do✌ 'MAP' milte hai 'map_1 and map_2.'")
                              print("Aap kon se 'MAP' lena chate hai..?")
                              right_ans4 = input("[Tpye 1 :for map_1 and 2 :for map_2]=>")
                              if right_ans4 == "1":
                                     print("☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠")
                                     print("Nice..")
                                     print("OOPS, Ye 'MAP' mai kuch nahi likha hai. Yhe Map Galat hai.")
                                     print("You LOOSE...😥\n PLAY AGAIN😫")
                              elif right_ans4 == "2":
                                     print("☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠")
                                     print("Ye sahi map hai jo 'HIDDEN VILLAGE' ka rasta batata hai")
                                     print("YOU WIN..........😍😍")
                                     print("YOU WIN..........😍😍")
                                     print("YOU WIN..........😍😍")
                                     print("YOU WIN..........😍😍")
                              else:
                                   print("☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠")
                                   print("Invalid input😑..Please Plya Again")  
                       elif right_ans3 == "2":
                              print("☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠")
                              print("Okay, You Choose tunnel_2")
                              print("OOPS, Yha par tho ek 'Monster' hai ")
                              print("=>Kya aap uss 'Monster' se fight karna chate ho ye fir back jaane chate ho..?")
                              right_ans5 = input("[Type Fight :for Fight and Back :for Go Back]=> ").lower()
                              if right_ans5 =="fight":
                                     print("☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠")
                                     print("OOPS 'monster' aap se jada strong hai isley aap figth mai maare gye😶 ")
                                     print("You LOOSE..😥\n PLAY AGAIN")
                              elif right_ans5 == "back":
                                     print("☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠")
                                     print("OOPS Tunnel ka gate band ho gaya hai.")
                                     print("Oor AAP 'Monster ke hatho maare gaye'")
                                     print("You LOOSE...😥\n PLAY AGAIN")
                              else:
                                print("☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠")
                                print("Invalid input😑..Please Plya Again")
                              
                       else:
                            print("☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠")
                            print("Invalid input😑..Please Plya Again")      
                              
                else:
                       print("Invalid input😑..Please Plya Again")
                       
        elif right_ans1 == "back":
                print("☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠")
                print("OOPS..")
                print("You LOOSE.. 'back' jaate samay aap par ek bada sa tree gira oor aap mar gaye..😥 ")
        else:
            print("☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠")
            print("Invalid input😑..Please Plya Again")
else:
        print("☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠")
        print("Invalid Input😑..Please Play Again")
        
  
    