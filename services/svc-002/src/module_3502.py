"""Service module 3502: business logic, no crypto."""


def calculate_total_3502(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3502():
    return 'module 3502 handles orders and invoices'
