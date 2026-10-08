"""Service module 853: business logic, no crypto."""


def calculate_total_853(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_853():
    return 'module 853 handles orders and invoices'
