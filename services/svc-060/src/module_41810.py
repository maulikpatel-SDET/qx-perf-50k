"""Service module 41810: business logic, no crypto."""


def calculate_total_41810(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41810():
    return 'module 41810 handles orders and invoices'
