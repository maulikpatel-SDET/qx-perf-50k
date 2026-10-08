"""Service module 26260: business logic, no crypto."""


def calculate_total_26260(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26260():
    return 'module 26260 handles orders and invoices'
