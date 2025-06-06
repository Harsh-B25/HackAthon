// stats.js
document.addEventListener("DOMContentLoaded", () => {
  const counters = document.querySelectorAll(".stat-number");

  counters.forEach((counter) => {
    const targetText = counter.innerText;
    const target = parseFloat(targetText.replace(/[^\d.]/g, ""));
    const suffix = targetText.replace(/[\d.]/g, "");

    let count = 0;
    const isDecimal = targetText.includes(".");
    const increment = target / 100;

    const updateCount = () => {
      count += increment;
      if (count >= target) {
        counter.innerText = targetText;
      } else {
        counter.innerText =
          (isDecimal ? count.toFixed(1) : Math.floor(count)) + suffix;
        requestAnimationFrame(updateCount);
      }
    };

    updateCount();
  });
});

// features.js
// features.js
document.addEventListener("DOMContentLoaded", () => {
    const paragraphs = document.querySelectorAll(".feature-card p");

    const options = {
        threshold: 0.6 // Trigger when 60% of the card is visible
    };

    const typeText = (element, text) => {
        element.innerText = "";
        let i = 0;

        function typeChar() {
            if (i < text.length) {
                element.innerHTML += text.charAt(i);
                i++;
                setTimeout(typeChar, 25);
            }
        }

        typeChar();
    };

    const observer = new IntersectionObserver((entries, obs) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const para = entry.target;
                if (!para.dataset.typed) { // prevent retyping on scroll out/in
                    para.dataset.typed = "true";
                    typeText(para, para.dataset.fulltext);
                }
                obs.unobserve(para); // Remove after first trigger
            }
        });
    }, options);

    paragraphs.forEach(p => {
        p.dataset.fulltext = p.innerText;
        p.innerText = "";
        observer.observe(p);
    });
});


const upload_area = document.querySelectorAll(".upload-area");
const input_choose = document.querySelectorAll(".file_upload");
upload_area.forEach((upload,index) => {
  upload.addEventListener("click", () => {
    input_choose[index].click();
  });
});
  