# 블록을 화면 중앙에 정렬하는 html&css 코드

```html
<!-- CSS 부분-->
<style>
html, body{    
    height: 100%;
}

body{    
    display: table;    
    margin: 0 auto;
}

.container{
    height: 100%;    
    display: table-cell;    
    vertical-align: middle;
}

.main{    
    height: 200px;    
    width: 200px;    
    background-color: blue;      
}
</style>

<!-- 본문 부분 -->

<div class="container">    
    <div class="main">
    </div>    
</div>
```

source : https://stackoverflow.com/questions/17520145/center-a-div-horizontally-and-vertically-and-keep-centered-when-resizing-the-par