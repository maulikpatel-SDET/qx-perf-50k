"""Service module 35183: business logic, no crypto."""


def calculate_total_35183(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35183():
    return 'module 35183 handles orders and invoices'
