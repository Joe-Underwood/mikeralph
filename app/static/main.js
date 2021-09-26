const vm = new Vue({
    el: '#root',
    delimiters: ['<%', '%>'],
    data: {
        publicProductList: []
    },
    created: function() {
        this.getPublicProductList();
    },
    methods: {
        getPublicProductList() {
            const response =
                fetch('/get_public_product_list', { method: 'post' })
                    .then(response => {
                        return response.json();
                    })
                    .then(json => {
                        this.publicProductList = json['publicProductList'];
                        return json['publicProductList'];
                    })
                
            return response;
        }
    }
})