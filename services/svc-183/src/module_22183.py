"""Service module 22183: business logic, no crypto."""


def calculate_total_22183(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22183():
    return 'module 22183 handles orders and invoices'
