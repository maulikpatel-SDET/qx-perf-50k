"""Service module 27071: business logic, no crypto."""


def calculate_total_27071(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27071():
    return 'module 27071 handles orders and invoices'
