"""Service module 38706: business logic, no crypto."""


def calculate_total_38706(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38706():
    return 'module 38706 handles orders and invoices'
