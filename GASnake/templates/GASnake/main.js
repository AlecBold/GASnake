const Engine = window.engine;
const Display = window.display;
const getData = window.utils.getData;

const COLOR = {
    snake: 'white',
    apple: 'red',
    background: 'grey',
};

const UNITS = {
    ratio: 1,
    maxCord: 25,
    padding: 30,

    snakeSize: 15,
    appleSize: 15,

    updateRate: 1000 / 10,
};

window.addEventListener('load', () => {
    const screen = document.querySelector('#screen');
    const display = new Display(screen, UNITS.snakeSize, UNITS.appleSize,  UNITS.maxCord);

    let data;
    let engine;
    let dataIndex = 0;

    function render () {
        if(data[dataIndex]) {
            const {snake, apple} = data[dataIndex];

            display.fill(COLOR.background);
            display.snake(snake, COLOR.snake);
            display.apple(apple, COLOR.apple);
        }
    }

    function update() {
        if(dataIndex > data.length) {
            engine.stop();
            getData().then(newData => {
                data = newData;
                dataIndex = 0;
                engine.start();
            });
        } else {
            dataIndex += 1;
        }
    };

    function resize() {
        const width = document.documentElement.clientWidth - UNITS.padding;
        const height = document.documentElement.clientHeight - UNITS.padding;

        display.resize(width, height, UNITS.ratio);
    }

    (async function init() {
        data = await getData();
        engine = new Engine(UNITS.updateRate, update, render);

        resize(); 
        engine.start();
        window.addEventListener('resize', resize);
    })();
});