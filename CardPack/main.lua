require('background')

function love.load()
    background:load()
    cardPack = love.graphics.newImage("assets/img/gigaPika.png")
    graspHand = love.graphics.newImage("assets/img/holdHand.png")
end

function love.draw()
    background:draw()
    love.graphics.draw(graspHand, 250,150)
end

-- sudo
-- 
-- Walkup to Isle 
-- hand reach out half way -> press start -> Reach and grab card
-- Fade out -> fade In -> hand holding card pack, spacebar mash to fill bar -> rips open card 
-- Cards pop up, one by one to click and drag of asset to toss or keep in book
