(() => {
    class Engine {
        constructor(timeStep, update, render) {
            this.accumulatedTime = 0;
            this.timeStep = timeStep;
            this.updated = false;
    
            this.update = update;
            this.render = render;
            this.runHandler = this.run.bind(this);
        }
    
        run(timeStamp) {
            this.accumulatedTime += timeStamp - this.time;
            this.time = timeStamp;
            this.animationFrameRequest = window.requestAnimationFrame(this.runHandler);
    
            if (this.accumulatedTime >= this.timeStep * 3) {
                this.accumulatedTime = this.timeStep;
            }
    
            while(this.accumulatedTime >= this.timeStep) {
                this.accumulatedTime -= this.timeStep;
                this.update();
                this.updated = true;
            }
    
            if (this.updated) {
                this.updated = false;
                this.render()
            }
        }
    
        start() {
            this.accumulatedTime = this.timeStep;
            this.time = window.performance.now();
            this.animationFrameRequest = window.requestAnimationFrame(this.runHandler);
        }
    
        stop() {
            window.cancelAnimationFrame(this.animationFrameRequest);
        }
    
    };

    window.engine = Engine;
})();
