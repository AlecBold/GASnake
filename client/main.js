const Engine = window.engine;
const Display = window.display;
const getData = window.utils.getData;

const COLOR = {
    snake: '#eeeeee',
    apple: '#d65a31',
    background: '#393e46',
};

const UNITS = {
    dpr:  window.devicePixelRatio || 1,
    aspectRatio: 1,
    maxXY: 25,
    padding: 30,

    snakeSize: 15,
    appleSize: 15,

    updateRate: 1000 / 10,
};

const DISPLAY_UNITS = {
    dpr:  window.devicePixelRatio || 1,
    aspectRatio: 1,
    maxXY: 25,
    snakeSize: 15,
    appleSize: 15,
}

const SNAKE_DATA_URL = '/coords.json';

// TODO: render via buffer (solve hight dpr problem)
// TODO: make snake & apple size scalable
// TODO: error handling

window.addEventListener('load', () => {
    const canvas = document.querySelector('#screen');
    const display = new Display({canvas: canvas, ...UNITS});

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
            getData(SNAKE_DATA_URL).then(newData => {
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

        display.resize(width, height, UNITS.aspectRatio);
    }

    (async function init() {
        data = await getData(SNAKE_DATA_URL);
        engine = new Engine(UNITS.updateRate, update, render);

        resize(); 
        engine.start();
        window.addEventListener('resize', resize);
    })();
});