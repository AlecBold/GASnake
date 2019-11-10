(() => {
    class Display {
        constructor(screen, snakeSize = 15, appleSize = 10, maxCord) {
            this.canvas = screen;
            this.ctx = screen.getContext('2d');

            this.maxCord = maxCord;
            this.snakeSize = snakeSize;
            this.appleSize = appleSize;
        }

        interpolate(coords) {
            const coordsRatio = this.canvas.width / this.maxCord;

            return coords.map(coord => coord * coordsRatio);
        }

        drawRect(x, y, size, color) {
            this.ctx.fillStyle = color;
            this.ctx.fillRect(x,y, size, size)
        }

        snake(coords) {
            const color = 'white';
            const size = this.snakeSize;

            coords.forEach(coordinates => {
                const [x, y] = this.interpolate(coordinates);

                this.drawRect(x, y, size, color)
            })
        }

        apple(coords) {
            const [x, y] = this.interpolate(coords);
            const color = 'red';
            const size = this.appleSize;

            this.drawRect(x, y, size, color);
        }

        fill(color) {
            this.ctx.fillStyle = color;
            this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
        }
        
        resize(width, height, heightWidthRatio) {
            if(height > width) {
                this.canvas.height = width * heightWidthRatio;
                this.canvas.width = width;
            } else {
                this.canvas.height = height;
                this.canvas.width = height / heightWidthRatio;
            }
        }
    }

    window.display = Display;
})()