// choices-enhancer.js
document.addEventListener('DOMContentLoaded', function () {
  const selectEl = document.getElementById('filter_result');

  const choices = new Choices(selectEl, {
    removeItemButton: true,
    allowHTML: true,
    placeholderValue: 'Select result...',
    noResultsText: 'No result found',
    noChoicesText: 'No choices available',
  });

  const dropdownList = selectEl.closest('.choices').querySelector('.choices__list--dropdown');

  if (dropdownList && !dropdownList.querySelector('.choices-actions')) {
    const actionRow = document.createElement('div');
    actionRow.className = 'choices-actions';

    const btnSetAll = document.createElement('button');
    btnSetAll.className = 'btn btn-outline-primary btn-sm';
    btnSetAll.type = 'button';
    btnSetAll.textContent = 'SET';
    btnSetAll.setAttribute('aria-label', 'Select all options');

    const btnUnsetAll = document.createElement('button');
    btnUnsetAll.className = 'btn btn-outline-secondary btn-sm';
    btnUnsetAll.type = 'button';
    btnUnsetAll.textContent = 'UNSET';
    btnUnsetAll.setAttribute('aria-label', 'Clear all selected options');

    actionRow.appendChild(btnSetAll);
    actionRow.appendChild(btnUnsetAll);
    dropdownList.prepend(actionRow);

    // SET: Select all options
    btnSetAll.addEventListener('click', () => {
      choices.removeActiveItems();
      const allValues = [...selectEl.options].map(opt => opt.value);
      allValues.forEach(val => choices.setChoiceByValue(val));
    });

    // UNSET: Clear all selected options
    btnUnsetAll.addEventListener('click', () => {
      choices.removeActiveItems();
    });
  }
});