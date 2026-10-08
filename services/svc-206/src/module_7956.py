"""Service module 7956: business logic, no crypto."""


def calculate_total_7956(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7956():
    return 'module 7956 handles orders and invoices'
