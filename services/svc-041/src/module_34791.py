"""Service module 34791: business logic, no crypto."""


def calculate_total_34791(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34791():
    return 'module 34791 handles orders and invoices'
