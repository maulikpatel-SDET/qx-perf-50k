"""Service module 5375: business logic, no crypto."""


def calculate_total_5375(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5375():
    return 'module 5375 handles orders and invoices'
