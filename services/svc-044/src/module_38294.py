"""Service module 38294: business logic, no crypto."""


def calculate_total_38294(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38294():
    return 'module 38294 handles orders and invoices'
