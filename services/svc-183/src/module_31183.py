"""Service module 31183: business logic, no crypto."""


def calculate_total_31183(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31183():
    return 'module 31183 handles orders and invoices'
