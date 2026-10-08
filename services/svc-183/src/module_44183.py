"""Service module 44183: business logic, no crypto."""


def calculate_total_44183(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44183():
    return 'module 44183 handles orders and invoices'
