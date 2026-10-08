"""Service module 46260: business logic, no crypto."""


def calculate_total_46260(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46260():
    return 'module 46260 handles orders and invoices'
