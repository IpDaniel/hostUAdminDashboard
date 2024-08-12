function toggleDropdown() {
    const content = document.getElementById('dropdown-content');
    const downArrow = document.getElementById('sql-query-down-arrow');
    const upArrow = document.getElementById('sql-query-up-arrow');
    const header = document.getElementById('sql-query-header');
    if (upArrow.style.visibility === 'hidden') {
        upArrow.style.visibility = 'visible';
        downArrow.style.visibility = 'hidden';
        upArrow.style.marginLeft = '-30px';
        header.style.marginLeft = '0px'
    } else {
        upArrow.style.visibility = 'hidden';
        downArrow.style.visibility = 'visible';
        header.style.marginLeft = '0px'
    }
    content.classList.toggle('show');
}