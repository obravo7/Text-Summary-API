
function summarize_text() {
      var long_text = document.getElementById("input-text").value;
      console.log(long_text);
      document.getElementById("long-text").innerHTML = long_text;

      // run text summary
      console.log('running text summarization...');
      fetch('http://localhost:5000/api/v1/summarize', {
        method: 'POST',
        headers: {
          'Content-type': 'application/x-www-form-urlencoded'
        },
        body: new URLSearchParams({
          'text': long_text
        })
      }).then(res => res.json())
        .then(res => {
          console.log('finished fetching sources...');
          document.getElementById("text-summary").innerHTML = res['summary'];
          document.getElementById("summary-id").innerHTML = res['summary_id'];
        });
}

function get_summary() {
      var summary_id = document.getElementById("input-id").value;
      console.log(summary_id);

      console.log('fetching text summary using ID...');
      fetch('http://localhost:5000/api/v1/get_summary', {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          summary_id: summary_id
        })
      }).then(res => res.json())
        .then(res => {
          console.log(res);

          // update original text and summary text fields.
          document.getElementById("long-text").innerHTML = res["long_text"];
          document.getElementById("text-summary").innerHTML = res['text_summary'];
          document.getElementById("summary-id").innerHTML = summary_id;
          });

}