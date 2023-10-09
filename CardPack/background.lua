background = {}

function background:load()
    self.cardRack = love.graphics.newImage("assets/img/heaven.jpg")
end

function background:update(dt)

end

function background:draw()
    love.graphics.draw(self.cardRack, 0, 0)
end
