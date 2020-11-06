
 let comment_component = Vue.component('comment-component', {
    data: function () {
        return {
            confirm_delete_comment: false,

            profile_id: profile_id
            // current_profile_id: JSON.parse("{% if profile %}{{profile.id}}{%else%}0{%endif%}")
        }
    },
    methods: {
        ShowConfirmDeleteComment: function () {

            this.confirm_delete_comment = true
        },
        ConfirmDeleteComment: function (comment_id) {


            this.confirm_delete_comment = false
            let url = delete_comment_url
            let posting = $.post(url, {
                comment_id: comment_id,
                csrfmiddlewaretoken: csrfmiddlewaretoken
            })

            posting.done(function (data) {
                console.log(data)
                if (data.result === 'SUCCEED') {
                    comment_app.comments=data.comments
                }
            })


        },
        CancelDeleteComment: function () {
            this.confirm_delete_comment = false
        },
    },
    props: ['comment'],
    template: comment_template,
})

