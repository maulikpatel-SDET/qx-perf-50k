"""Service module 33805: business logic, no crypto."""


def calculate_total_33805(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33805():
    return 'module 33805 handles orders and invoices'
