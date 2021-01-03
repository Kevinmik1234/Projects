

Screen_build = """
ScreenManager:
   
    ClassScreen:
    WindowManager:
    BeginnerScreen:
    IntermediateScreen:
    AdvancedScreen:
    


       
<ClassScreen>:
    name: 'class'
    Screen:
        
            
        canvas.before:
            Rectangle:
                pos: self.pos
                size: self.size
                source: '5.jpg'
        BoxLayout:
            orientation: 'vertical'
            
            Widget:
            ScrollView:    
                MDList:
                    OneLineIconListItem:
                        text: 'Match Winning Tips'
                        theme_text_color: 'Custom'
                        text_color: (0/255.0, 255/255.0, 0/255.0, 1)
                        on_release:
                            root.manager.current = 'basic'
                        IconLeftWidget:
                            icon: 'soccer.png' 
                            on_press:
                                root.manager.current = 'basic'
                    OneLineIconListItem:
                        text: 'Training Players'
                        theme_text_color: 'Custom'
                        text_color: (0/255.0, 255/255.0, 0/255.0, 1)
                        on_release:
                            root.manager.current = 'mediate'
                        IconLeftWidget:
                            icon: 'soccer-boots.png'
                            on_press:
                                root.manager_current = 'mediate'
                            
                    OneLineIconListItem:
                        text: 'Winning More Games'
                        theme_text_color: 'Custom'
                        text_color: (0/255.0, 255/255.0, 0/255.0, 1)
                        on_release:
                            root.manager.current = 'first'
                        IconLeftWidget:
                            icon: 'soccer-field.png'
                            on_release:
                                root.manager.current = 'first'
                    OneLineIconListItem:
                        text: 'Becoming A Top Manager'
                        theme_text_color: 'Custom'
                        text_color: (0/255.0, 255/255.0, 0/255.0, 1)
                        on_release:
                            root.manager.current = 'proff'
                        IconLeftWidget:
                            icon: 'football-players.png'
                            on_release:
                                root.manager.current = 'proff'
            Widget:
            
        NavigationLayout:
            ScreenManager:
                Screen:
                    
                    
                    
                   
                    
                 
                    
                    BoxLayout:
                        orientation: 'vertical'
                        MDToolbar:
                            title: 'Tips and Guide'
                            left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
                            elevation: 10
                        MDBottomAppBar:
                            MDToolbar:
                                title: 'Tips and Guide'
                                type: 'bottom'
                                icon: 'icon.ico'
                                mode: 'end'
                                left_action_items: [['coffee', lambda x: app.coffee()]]
                        
                        
                        Widget:
            MDNavigationDrawer:
                id: nav_drawer
                BoxLayout:
                    orientation: 'vertical'
                    
                    MDList:
                     
                        OneLineIconListItem:
                            text: 'THEME'
                            on_release:
                                app.show_theme()
                            IconLeftWidget:
                                icon: 'theme-light-dark'
                                on_release:
                                    app.show_theme()
                        OneLineIconListItem:
                            text: 'QUIT'
                            on_release:
                                app.quit_data()
                            IconLeftWidget:
                                icon: 'logout'
                                on_release:
                                    app.quit_data()
           
                    
                   


                            
                    Image:
                        source: 'Me.png'
                        pos_hint: {'center_y': 0.9}
<WindowManager>:
    name: 'first'
    Screen:
        canvas.before:
            Rectangle:
                pos: self.pos
                size: self.size
                source: 'ball.png'
        NavigationLayout:
            ScreenManager:
                Screen:
                    BoxLayout:
                        orientation: 'vertical'
                        
                        MDBottomAppBar:
                            MDToolbar:
                                title: 'Winning Games'
                                type: 'bottom'
                                icon: 'soccer-field.png'
                                mode: 'end'
                                left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
                    BoxLayout:
                        orientation: 'vertical'
                        ScrollView:
                            MDList:
                                theme_text_color: 'Custom'
                                text_color: (243/255.0, 19/255.0, 78/255.0, 1)
                                ThreeLineListItem:
                                    theme_text_color: 'Custom'
                                    text_color: (243/255.0, 19/255.0, 78/255.0, 1)
                                    text: "1.Use C Button To Switch Defenders "
                                    secondary_text: 'Using C button to switch defenders'
                                    tertiary_text: 'will help in stopping opponents'
                                
                                ThreeLineListItem:
                                    theme_text_color: 'Custom'
                                    text_color: (243/255.0, 19/255.0, 78/255.0, 1)
                                    text: "2. Watch Ads After Each Game For Coins"
                                    secondary_text: 'Watch Ads for coins '
                                    tertiary_text: 'to buy and upgrade '
                                
                                ThreeLineListItem:
                                    theme_text_color: 'Custom'
                                    text_color: (243/255.0, 19/255.0, 78/255.0, 1)
                                    text: " 3. Spend Gold To Improve Players"
                                    secondary_text: 'spend coins on upgrades'
                                    tertiary_text: 'to improve players ability'
                                ThreeLineListItem:
                                    text: "4. Saving Penalties"
                                    theme_text_color: 'Custom'
                                    text_color: (243/255.0, 19/255.0, 78/255.0, 1)
                                    secondary_text: 'the trick is to move to'
                                    tertiary_text: 'where player faces or opposite'
                                ThreeLineListItem:
                                    text: "5. Taking Outside Shots"
                                    theme_text_color: 'Custom'
                                    text_color: (243/255.0, 19/255.0, 78/255.0, 1)
                                    secondary_text: 'The trick, place your shots to be directly at'
                                    tertiary_text: 'goal, but a few distances from the golie'
                                ThreeLineListItem:
                                    text: "6. Thinking faster"
                                    theme_text_color: 'Custom'
                                    text_color: (243/255.0, 19/255.0, 78/255.0, 1)
                                    secondary_text: 'The golie usually comes off his lines'
                                    tertiary_text: 'so try to take advantage of that'
                                


            MDNavigationDrawer:
                id: nav_drawer
                BoxLayout:
                    orientation: 'vertical'
                    MDList:
                        OneLineIconListItem:
                            text: 'Home'
                            on_release:
                                root.manager.current = 'class'
                            IconLeftWidget:
                                icon: 'home'
                                on_release:
                                    root.manager.current = 'class'
                        OneLineIconListItem:
                            text: 'THEME'
                            on_release:
                                app.show_theme()
                            IconLeftWidget:
                                icon: 'theme-light-dark'
                                on_release:
                                    app.show_theme()
                        OneLineIconListItem:
                            text: 'QUIT'
                            on_press:
                                app.quit_data()
                            IconLeftWidget:
                                icon: 'logout'
                                on_press:
                                    app.quit_data()
                            
                    Image:
                        source: 'Me.png'
                        pos_hint: {'center_y': 0.9}

<BeginnerScreen>:
    name: 'basic'
    Screen:
        canvas.before:
            Rectangle:
                pos: self.pos
                size: self.size
                source: 'soccer.png'
        NavigationLayout:
            ScreenManager:
                Screen:
                    BoxLayout:
                        orientation: 'vertical'
                        MDBottomAppBar:
                            MDToolbar:
                                title: 'Winning Tips'
                                type: 'bottom'
                                icon: 'soccer.png'
                                mode: 'end'
                                left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
                    BoxLayout:
                        orientation: 'vertical'
                   
                        ScrollView:
                             
                      
                            MDList:
                               
                                ThreeLineListItem:
                                    text: "1. Management Made Easy"
                                    secondary_text: 'watch for auto-subs by assistant'
                                    tertiary_text: ' coaches to avoid injuries'
                                    theme_text_color: 'Custom'
                                    text_color: (243/255.0, 19/255.0, 78/255.0, 1)
                                ThreeLineListItem:
                                    text: "2. Rage- Quitting"
                                    secondary_text: 'Do not quit under anger or Pressure,'
                                    tertiary_text: 'online games are more complex'
                                    theme_text_color: 'Custom'
                                    text_color: (243/255.0, 19/255.0, 78/255.0, 1)
                                ThreeLineListItem:
                                    text: " 3. Achieving Goals"
                                    secondary_text: 'Earn coins for upgrade'
                                    tertiary_text: 'by achieving goals'
                                    theme_text_color: 'Custom'
                                    text_color: (243/255.0, 19/255.0, 78/255.0, 1)
                                ThreeLineListItem:
                                    theme_text_color: 'Custom'
                                    text_color: (243/255.0, 19/255.0, 78/255.0, 1)
                                    text: "4.Hire High rated Coaches"
                                    secondary_text: 'Hire coaches that can help players'
                                    tertiary_text: 'reach their full potentials'
                                ThreeLineListItem:
                                    text: "5. Transfer Market"
                                    theme_text_color: 'Custom'
                                    text_color: (243/255.0, 19/255.0, 78/255.0, 1)
                                    secondary_text: 'Use transfer market wisely by buying'
                                    tertiary_text: 'players of high demand in your team'
                                ThreeLineListItem:
                                    theme_text_color: 'Custom'
                                    text_color: (243/255.0, 19/255.0, 78/255.0, 1)
                                    text: "6. Understand The Controls more"
                                    secondary_text: 'Avoid pressing random buttons  but'
                                    tertiary_text: 'always try understand the controls'
                                
                    BoxLayout:
                        orientation: 'vertical'

                        Widget:                    
                        
                   
                        
                        


            MDNavigationDrawer:
                id: nav_drawer
                BoxLayout:
                    orientation: 'vertical'
                    MDList:
                     
                        OneLineIconListItem:
                            text: 'Home'
                            on_release:
                                root.manager.current = 'class'
                            IconLeftWidget:
                                icon: 'home'
                                on_release:
                                    root.manager.current = 'class'
                        OneLineIconListItem:
                            text: 'THEME'
                            on_release:
                                app.show_theme()
                            IconLeftWidget:
                                icon: 'theme-light-dark'
                                on_release:
                                    app.show_theme()
                        OneLineIconListItem:
                            text: 'QUIT'
                            on_press:
                                app.quit_data()
                            IconLeftWidget:
                                icon: 'logout'
                                on_release:
                                    app.quit_data()
                            
                    Image:
                        source: 'Me.png'
                        pos_hint: {'center_y': 0.9}
                
                    
                    Widget:
<IntermediateScreen>:
    name: 'mediate'
    Screen:
        canvas.before:
            Rectangle:
                pos: self.pos
                size: self.size
                source: 'football-players.png'
        NavigationLayout:
            ScreenManager:
                Screen:
                    BoxLayout:
                        orientation: 'vertical'
                        MDBottomAppBar:
                            MDToolbar:
                                icon: 'soccer-boots.png'
                                title: 'Training Players'
                                type: 'bottom'
                                mode: 'end'
                                left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
                                
                  
                    BoxLayout:
                        orientation: 'vertical'
                        
                        ScrollView:
                             
                      
                            MDList:
                                
                                
                                ThreeLineListItem:
                                    text: "1. Understand Each Player’s Ratings"
                                    secondary_text: ' understand the players abilities '
                                    tertiary_text: 'it helps  when it comes to selection'
                                    theme_text_color: 'Custom'
                                    text_color: (243/255.0, 19/255.0, 78/255.0, 1)
                                    
                                ThreeLineListItem:
                                    theme_text_color: 'Custom'
                                    text_color: (243/255.0, 19/255.0, 78/255.0, 1)
                                    text: "2. Form Boosts "
                                    secondary_text: 'tap players and press the form boost'
                                    tertiary_text: 'to help boost the form of players'
                                
                                ThreeLineListItem:
                                    theme_text_color: 'Custom'
                                    text_color: (243/255.0, 19/255.0, 78/255.0, 1)
                                    text: " 3. Hire Great Coaches"
                                    secondary_text: 'Hire coaches to boost players'
                                    tertiary_text: 'also for fitness and technic'
                                    
                                ThreeLineListItem:
                                    theme_text_color: 'Custom'
                                    text_color: (243/255.0, 19/255.0, 78/255.0, 1)
                                    text: " 4.Release Players for Coaches"
                                    secondary_text: 'Release weaker players for'
                                    tertiary_text: 'fitness and technical coaches'
                                ThreeLineListItem:
                                    theme_text_color: 'Custom'
                                    text_color: (243/255.0, 19/255.0, 78/255.0, 1)
                                    text: "5.Healing Revives players"
                                    secondary_text: 'revive players through healing,'
                                    tertiary_text: 'helps in providing more energy '
                                ThreeLineListItem:
                                    theme_text_color: 'Custom'
                                    text_color: (243/255.0, 19/255.0, 78/255.0, 1)
                                    text: "6.Reach The Objectives for Gems"
                                    secondary_text: 'Reaching season objectives will '
                                    tertiary_text: 'help in obtaining more gems'
                                   
          
                                    
                       
                      
                    
                    BoxLayout:
                        orientation: 'vertical'
                        
        
                        Widget:
            MDNavigationDrawer:
                id: nav_drawer
                BoxLayout:
                    orientation: 'vertical'
                    MDList:
                        OneLineIconListItem:
                            text: 'Home'
                            on_release:
                                root.manager.current = 'class'
                            IconLeftWidget:
                                icon: 'home'
                                on_release:
                                    root.manager.current = 'class'
                        OneLineIconListItem:
                            text: 'THEME'
                            on_release:
                                app.show_theme()
                            IconLeftWidget:
                                icon: 'theme-light-dark'
                                on_release:
                                    app.show_theme()
                        OneLineIconListItem:
                            text: 'QUIT'
                            on_release:
                                app.quit_data()
                            IconLeftWidget:
                                icon: 'logout'
                                on_release:
                                    app.quit_data()
                            
                    Image:
                        source: 'Me.png'
                        pos_hint: {'center_y': 0.9}
<AdvancedScreen>:
    name: 'proff'
    Screen:
        canvas.before:
            Rectangle:
                pos: self.pos
                size: self.size
                source: 'soccer-boots.png'
            
        NavigationLayout:
            ScreenManager:
                Screen:
                   

                    BoxLayout:
                        orientation: 'vertical'
                        MDBottomAppBar:
                            MDToolbar:
                                title: 'Top Manager'
                                type: 'bottom'
                                mode: 'end'
                                icon: 'football-players.png'
                                left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
                    BoxLayout:
                        orientation: 'vertical'  
                        ScrollView:  
                            MDList:
                                ThreeLineListItem:
                                    text: "1. Basics"
                                    secondary_text: 'Control the game both on offence'
                                    tertiary_text: 'and defence'
                                    theme_text_color: 'Custom'
                                    text_color: (243/255.0, 19/255.0, 78/255.0, 1)
                                ThreeLineListItem:
                                    text: "2.Everything Matters On The Pitch"
                                    secondary_text: 'keep your eyes on the ball,'
                                    tertiary_text: 'on the players and the opposition team'
                                    theme_text_color: 'Custom'
                                    text_color: (243/255.0, 19/255.0, 78/255.0, 1)
                                ThreeLineListItem:
                                    text: " 3. Tactics"
                                    secondary_text: 'Make sure you organise your team in '
                                    tertiary_text: 'the best formation of your tactics'
                                    theme_text_color: 'Custom'
                                    text_color: (243/255.0, 19/255.0, 78/255.0, 1)
                                ThreeLineListItem:
                                    theme_text_color: 'Custom'
                                    text_color: (243/255.0, 19/255.0, 78/255.0, 1)
                                    text: "4.Dont be too predictable"
                                    secondary_text: 'Human opponents can predict '
                                    tertiary_text: 'your plan .So, be flexible'
                                ThreeLineListItem:
                                    theme_text_color: 'Custom'
                                    text_color: (243/255.0, 19/255.0, 78/255.0, 1)
                                    text: "5. Defence"
                                    secondary_text: 'use the B button to gain'
                                    tertiary_text: 'possession, and C to switch'
                                ThreeLineListItem:
                                    theme_text_color: 'Custom'
                                    text_color: (243/255.0, 19/255.0, 78/255.0, 1)
                                    text: "6. Dont Be Too Aggresive When Tackling"
                                    secondary_text: 'Aggresive tackling could get'
                                    tertiary_text: 'you booked and suspended'
                                    
                        
            MDNavigationDrawer:
                id: nav_drawer
                BoxLayout:
                    orientation: 'vertical'
                    MDList:
                        OneLineIconListItem:
                            text: 'Home'
                            on_release:
                                root.manager.current = 'class'
                            IconLeftWidget:
                                icon: 'home'
                                on_release:
                                    root.manager.current = 'class'
                        
                        OneLineIconListItem:
                            text: 'THEME'
                            on_release:
                                app.show_theme()
                            IconLeftWidget:
                                icon: 'theme-light-dark'
                                on_release:
                                    app.show_theme()
                        OneLineIconListItem:
                            text: 'QUIT'
                            on_release:
                                app.quit_data()
                            IconLeftWidget:
                                icon: 'logout'
                                on_release:
                                    app.quit_data()
                            
                    Image:
                        source: 'Me.png'
                        pos_hint: {'center_y': 0.9}
<ThemeScreen>:
    name: 'theme'
    Screen:
        NavigationLayout:
            ScreenManager:
                Screen:
                    
                    

                    BoxLayout:
                        orientation: 'vertical'
                        MDToolbar:
                            title: 'Theme Picker'
                            left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
                            elevation: 10
                        Widget:
            MDNavigationDrawer:
                id: nav_drawer
                BoxLayout:
                    orientation: 'vertical'
                    MDList:
                        OneLineIconListItem:
                            text: 'MATCH WINNING TIPS'
                            on_release:
                                root.manager.current = 'basic'
                            IconLeftWidget:
                                icon: 'book' 
                                on_release:
                                    root.manager.current = 'basic'
                        OneLineIconListItem:
                            text: 'TRAINING YOUR PLAYERS'
                            on_release:
                                root.manager.current = 'mediate'
                            IconLeftWidget:
                                icon: 'head-flash'
                                on_release:
                                    root.manager_current = 'mediate'
                                
                        OneLineIconListItem:
                            text: 'WINNING MORE GAMES'
                            on_release:
                                root.manager.current = 'proff'
                            IconLeftWidget:
                                icon: 'head-lightbulb'
                                on_release:
                                    root.manager.current = 'proff'
                        OneLineIconListItem:
                            text: 'BECOMING A TOP MANAGER'
                            on_release:
                                root.manager.current = 'proff'
                            IconLeftWidget:
                                icon: 'head-lightbulb'
                                on_release:
                                    root.manager.current = 'proff'
                        OneLineIconListItem:
                            text: 'THEME'
                            on_release:
                                app.show_theme()
                            IconLeftWidget:
                                icon: 'theme-light-dark'
                                on_release:
                                    app.show_theme()
                        OneLineIconListItem:
                            text: 'QUIT'
                            on_release:
                                quit()
                            IconLeftWidget:
                                icon: 'logout'
                                on_release:
                                    quit()
                            
                    Image:
                        source: 'Me.png'
                        pos_hint: {'center_y': 0.9}
    
    

"""


