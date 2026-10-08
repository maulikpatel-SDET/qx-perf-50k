"""Service module 27581: business logic, no crypto."""


def calculate_total_27581(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27581():
    return 'module 27581 handles orders and invoices'
