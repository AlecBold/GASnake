(() => {
    class Display {
        constructor({canvas, snakeSize, appleSize, maxXY, dpr}) {
            this.canvas = canvas;
            this.ctx = canvas.getContext('2d');

            this.maxCord = maxXY; 
            this.snakeSize = snakeSize;
            this.appleSize = appleSize;

            this.ctx.scale(dpr, dpr);
        }

        interpolate(coords) {
            const coordsRatio = this.canvas.width / this.maxCord;

            return coords.map(coord => coord * coordsRatio);
        }

        drawRect(x, y, size, color) {
            this.ctx.fillStyle = color;
            this.ctx.fillRect(x,y, size, size)
        }

        snake(coords, color) {
            const size = this.snakeSize;

            coords.forEach(coordinates => {
                const [x, y] = this.interpolate(coordinates);

                this.drawRect(x, y, size, color)
            })
        }

        apple(coords, color) {
            const [x, y] = this.interpolate(coords);
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