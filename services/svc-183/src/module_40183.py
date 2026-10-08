"""Service module 40183: business logic, no crypto."""


def calculate_total_40183(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40183():
    return 'module 40183 handles orders and invoices'
