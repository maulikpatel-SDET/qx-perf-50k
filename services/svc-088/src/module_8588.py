"""Service module 8588: business logic, no crypto."""


def calculate_total_8588(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8588():
    return 'module 8588 handles orders and invoices'
