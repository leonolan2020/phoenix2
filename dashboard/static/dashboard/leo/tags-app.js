
    var page_app = new Vue({
        el: "#app",
        data: {
            tags: tags,
            links: links,
            documents:documents,
            images: images,
            tag_title: '',
            document_title: '',
            document_file: '',
            link_title: '',
            link_url: '',
            image_title: '',
            image_description: '',
            image_location: '',
            show_add_image_panel: false,
        },
        methods: {
            add_document: function () {
                let title = app.document_title
                let url = "{% url 'dashboard:add_document' %}"
                let formData = new FormData();
                let file1 = $('#add-document-form')[0].elements[2].files[0]
                formData.append("file1", file1);
                formData.append("title", title);
                formData.append("csrfmiddlewaretoken", csrfmiddlewaretoken);
                formData.append("page_id", page_id);

                $.ajax({
                    url: url,
                    type: 'post',
                    data: formData,
                    contentType: false,
                    processData: false,
                    success: function (response) {
                        if (response != 0) {
                            if (response.result === 'SUCCEED') {
                                console.log(response)
                                page_app.documents = response.documents
                                // alert('file uploaded');
                                page_app.document_title = ''
                                page_app.document_file = ''
                            }
                        }
                        else {
                            // alert('file not uploaded');
                        }
                    },
                });

            }, add_link: function () {
                let title = page_app.link_title
                let url = "{% url 'dashboard:add_link' %}"
                let link_url = page_app.link_url

                var posting = $.post(url,
                    {
                        title: title,
                        url: link_url,
                        page_id: page_id,
                        csrfmiddlewaretoken: csrfmiddlewaretoken
                    }
                );

                // Put the results in a div
                posting.done(function (data) {
                    if (data.result === 'SUCCEED') {
                        page_app.links = data.links
                        page_app.link_title = ''
                        page_app.link_url = ''
                    }
                    else
                        console.log(data)
                })


            },
            remove_tag: function (tag_id) {
                let url = remove_tag_url

                var posting = $.post(url,
                    {
                        tag_id: tag_id,
                        page_id: page_id,
                        csrfmiddlewaretoken: csrfmiddlewaretoken
                    }
                );

                // Put the results in a div
                posting.done(function (data) {
                    console.log(data)
                    if (data.result === 'SUCCEED')
                    page_app.tags = data.tags
                })


            },
            add_tag: function (tag_id) {

                let url = add_tag_url

                var posting = $.post(url,
                    {
                        title: page_app.tag_title,
                        page_id: page_id,
                        csrfmiddlewaretoken: csrfmiddlewaretoken
                    }
                );

                // Put the results in a div
                posting.done(function (data) {
                    console.log(data)

                    if (data.result === 'SUCCEED') {
                        page_app.tags = data.tags
                        page_app.tag_title = ''
                    }
                })


            },
            add_image: function () {
                let title = app.image_title
                let description = app.image_description
                let location = app.image_location
                let url = "{% url 'dashboard:add_image' %}"
                let formData = new FormData();
                let image = $('#add-image-form')[0].elements[2].files[0]
                let thumbnail = $('#add-image-form')[0].elements[2].files[0]
                formData.append("thumbnail", thumbnail);
                formData.append("image", image);
                formData.append("title", title);
                formData.append("description", description);
                formData.append("location", location);
                formData.append("csrfmiddlewaretoken", csrfmiddlewaretoken);
                formData.append("page_id", page_id);

                $.ajax({
                    url: url,
                    type: 'post',
                    data: formData,
                    contentType: false,
                    processData: false,
                    success: function (response) {
                        if (response != 0) {
                            if (response.result === 'SUCCEED') {
                                page_app.images = response.images
                                // alert('file uploaded');
                                page_app.image_title = ''
                                page_app.image_description = ''
                                // app.image_location = ''
                                page_app.show_add_image_panel = false
                            }
                        }
                        else {
                            console.log(data)
                        }
                    },
                });


            }
        },
    })
