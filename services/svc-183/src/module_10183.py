"""Service module 10183: business logic, no crypto."""


def calculate_total_10183(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10183():
    return 'module 10183 handles orders and invoices'
